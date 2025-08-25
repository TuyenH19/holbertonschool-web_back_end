#!/usr/bin/env python3
"""
Test client module
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


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
