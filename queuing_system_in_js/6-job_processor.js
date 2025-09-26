import kue from 'kue';

const queue = kue.createQueue();

/**
 * Send a notification (logs per spec)
 * @param {string} phoneNumber
 * @param {string} message
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from "push_notification_code"
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data || {};
  // Basic guard (optional but helpful)
  if (!phoneNumber || !message) {
    return done(new Error('Missing phoneNumber or message'));
  }

  sendNotification(phoneNumber, message);
  done(); // triggers "complete" on the job for the creator script
});
