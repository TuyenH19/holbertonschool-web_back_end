// 7-job_processor.js
import kue from 'kue';

const queue = kue.createQueue();

// Blacklist
const blacklisted = ['4153518780', '4153518781'];

/**
 * Track progress + send (or fail if blacklisted)
 * @param {string} phoneNumber
 * @param {string} message
 * @param {kue.Job} job
 * @param {Function} done
 */
function sendNotification(phoneNumber, message, job, done) {
  // Start: 0%
  job.progress(0, 100);

  if (blacklisted.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Midway: 50%
  job.progress(50, 100);

  // Log the send action
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Finish
  return done();
}

// Process queue with concurrency 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data || {};
  return sendNotification(phoneNumber, message, job, done);
});
