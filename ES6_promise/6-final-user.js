// 6-final-user.js
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Call the signUpUser and uploadPhoto functions
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);

  // Wait for all promises to settle
  return Promise.allSettled([promise1, promise2])
    .then((results) =>
      // Map over the settled promises and return an array with status and value/error
      results.map((result) => ({
        status: result.status === 'fulfilled' ? 'fulfilled' : 'rejected',
        value: result.status === 'fulfilled' ? result.value : result.reason,
      }))
    );
}
