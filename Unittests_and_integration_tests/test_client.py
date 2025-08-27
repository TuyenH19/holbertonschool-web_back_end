#!/usr/bin/env python3
"""
Test client module
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized_class, parameterized
from client import GithubOrgClient

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org returns mocked payload;
        get_json called once with the org URL."""
        expected = {"login": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """_public_repos_url returns repos_url from the mocked org payload."""
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        # Patch the property-like `org` so no real HTTP is called
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock, return_value=payload):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos returns repo names;
        URL property and get_json called once."""
        # Test GithubOrgClient.public_repos returns the expected list
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = payload

        with patch.object(
            GithubOrgClient, "_public_repos_url",
                new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_url.return_value)

    @parameterized.expand([
        # repo has the correct license -> True
        ({"license": {"key": "my_license"}}, "my_license", True),
        # repo license is different -> False
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """has_license returns True only if
        repo['license']['key'] == license_key."""
        self.assertEqual(GithubOrgClient.has_license
                         (repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos with fixtures."""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and configure its side_effect."""
        # Patch requests.get where it’s imported (in utils)
        cls.get_patcher = patch("utils.requests.get")

        mock_get = cls.get_patcher.start()

        # Define mock responses based on URL
        def side_effect(url):
            mock_response = Mock()
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """public_repos returns expected repo list."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """public_repos with license filter returns only apache2 repos."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
