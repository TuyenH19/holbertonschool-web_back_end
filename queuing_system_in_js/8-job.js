import kue from 'kue';

/**
 * Create push notification jobs in Kue.
 * @param {Array<Object>} jobs - array of job data objects { phoneNumber, message }
 * @param {kue.Queue} queue - a Kue queue instance
 * @throws {Error} if jobs is not an array
 */
export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((data) => {
    const job = queue.create('push_notification_code_3', data);
    
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
  });
}
