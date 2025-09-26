import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create queue and enter test mode BEFORE running any tests
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear any jobs accumulated during a test
    queue.testMode.clear();
  });

  after(() => {
    // Exit test mode AFTER all tests
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue))
      .to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate jobs captured by kue's testMode
    expect(queue.testMode.jobs.length).to.equal(2);

    const [job1, job2] = queue.testMode.jobs;

    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data).to.deep.equal(jobs[0]);

    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.deep.equal(jobs[1]);
  });
});
