# Log Analysis Tool
Log Analysis tool is the first project prepared for Udacity Nanodegree. The project asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The reporting tool should answer these questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors? 

## Getting Started

In this project, I will use a PostgreSQL database, and build the system using Python3.

### Prerequisites

To start this tool you need to install these software:

* Linux virtual machine.
* Need Vagrant.
* Download the data [here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Add needs View to the database.

### Viewing
All these Viewings should applied to solve problem 3
so add these two viewings.

```
CREATE VIEW status_fail AS
select substring(cast(log.time as text), 0, 11) as day , count(*) as num_NotFound
    from log 
    where log.status = '404 NOT FOUND'
    group by day;
```

and 

```
CREATE VIEW status_log AS
select substring(cast(log.time as text), 0, 11) as day , count(*) as num_log
from log
group by day;
```

### Output

The output of these problems in the file above.




