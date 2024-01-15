Unless you're already using Airflow or similar job orchestration for your #dataengineering, especially for Spark jobs, then you may be in the same boat I've seen many others in depending on cron or Windows scheduler to call their #Python jobs. I've used SQL Agent in the past, even! 

This orchestration pattern shown here makes it easy to organize all your jobs into a package and leverage common code for easy extensibility. This example is just a start, where logging, scheduling, and error handling can be introduced to cover all your jobs. 

What this example does show is how easy it is to access separate job modules (or subpackages). It only takes a single parameter, but I recommend using configuration files, too. Given whatever job was requested, this executor will dispatch work to that job module (package). I also demonstrate how we log (print) something like the timing of the job execution. 

Do you use your own custom orchestration? Do you use a common orchestration like Airflow or Dagster? What are the biggest orchestration challenges you face?

<img src="../../static/0013.png" />
