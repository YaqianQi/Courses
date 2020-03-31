# Big Data Integration and Processing
## Data Retrieval
**Data Retrieval** 
**Qeury Language**
**Database Programming Language**
 1. **Structure Database:**
   - SQL Overview and Syntax 
   - Practice: Querying Relational Data with Postgres
 2. **Semistructured Database: MongoDB**
   - Syntax
   `db.collection.find(<query filter>,<projection>).<cursor modifier>`
   `from; where; select `
   - Example: 
    `select distinct beer, price from sells where price > 15`
    `db.sells.distinct({price:{$gt:15}, {beer:1, price:1,_id:0}})`
   - Operation: 
   `$eq, $gt, $gte, $lt, $lte, $ne, $in, $nin, $or, $and, $not, $nor`
   - Array Operation: 
     - find itens which are tagged as "popular" and organic
     `db.inventory.find({tags:{$in:["popular", "organic"]}})`
     - find 2nd and 3rf element of tags 
     `db.inventory.find({},{tags:{$slice:[1,2]}) -- skip 1, and return 2 rows`
     - find document whose 2nd element in tag is "summer`db.inventory.find(tags.1:"summer")`
   - Compound Statement 
     ```
     select * from inventory where (price = 3.99 or price = 4.99) and item !="Coors"
     ----------------------------------------------------------------------------
     db.inventory.find({
     $and :[
     {$or:[{price:3.99},{price:4.99}]},
     {item:{$ne:"Coors"}}
     ]
     })
     ```
   - On Counting and Distinct 
   ```
   select count(*) from Drinker 
   db.Drinker.count()
   ----------------------------------------
   select count(distinct addr) from Drinkers
   db.Drinker.count(addr:{$exists:true})
   ------------------------------------------
   select dictinct(places) from coutryDB
   db.countryDB.distinct(places) -- return [USA, France, Spain, UK]
   db.countryDB.distinct(places).length -- return 4
   
   ```
   - Aggregation Framework: grouping, sorting, aggregating framework 
   ```
   select cust_id as id, sum(amount) as total
   from order 
   where status = 'A'
   group by cust_id
   -----------------------------------------------
   db.order.aggregate([
   {$match: {status: 'A'}},
   {$group: {_id:"$cust_id",total:{$sum:"$amount"}}}
   ])
   ```
   - Join 
   ```
   select * from orders o
   join inventory i
   on o.item = i.sku
   --------------------------
   db.orders.aggregate([
      {$lookup:
      {from: "inventory",
      localField: "item",
      foreignField: "sku",
      as: "inventory_docs"
      }
   }
   ])
   ```
3. **Practice Query Documents in MongoDB** 
   - Exploring pandas dataframe 
 
## Information Integration 
- **Data Fusion**: Using data from subset of souces find the true value or true value distribution of a data item

## Processing Big Data 
1. **A Dataflow Approach** 
  - word count
    - map and reduce application 
    - "split -> map -> shuffle and sort" -> reduce == "split -> Do something -> merge"
       - map: parallelization over the input 
       - shuffle and sort: parallelization over intermediate data 
       - Reduce: parallezation over data group 
 - Data Transformations
   - Map: Apply same operation to each member of a collection 
   - Reduce: collecting things that have same 'key'
   - cross/cartesian: Do some process to each pair from two sets 
   - match/join: Do some process to each pair from two sets - which have same key.
   - Go-Group: group common items 
   - Filter: select elements that match a criteria 
 - Aggregations in Big Data Pipeline 
   - What is aggregation: 
     - group by, average, min, max, standard deviation, and, or, 
     - union, intersection, difference, concatenation
 - Analytical Operations: Pattern -> insights -> Decision 
   - Purpose: discover meaningful trends and patterns in data; gain insights into problem; make data-driven decison 
   - Sample Analytical Operation: Classification; Clustering; Path analysis; Connectivity analysis 
2. **Overview of Big Data Processing Systems**
  - Hadoop System: 
    - Coordination and workflow management: Acquire, prepare, analyze, report,act   
    - Data Integeration and Processing: Hive, pig, MapReduce, Yarn, Giraph, Storm, Spark, Flink
      - Excution Model: Batch, Steaming; latency; scalability; programming language; fault tolerance 
      - MapReuce: batch processing using disk storage; high latency; java; replication
      - Spark: batch and streaming processing using disk or memory storage; low-latency for small micro-batch size; scala, python, java, r
      - Flink: batch and steam processing using disk or memory storage; low-latency; java and scala 
      - Beam: batch and steam processing; low-latency; java and scala 
      - storm: steam processing; very low-latency; many programming languages
      - lambda architecture: 
        - batch layer(hadoop): batch processing/batch data collection 
        - speead layer(Storm): steam processing/real time data interfaces 
        - serving layer(Hase): Querying
      
    - Data Management and Storage: HDFS, Redis, gephi, mongodb, slor, certica    
 
 3. **Introduction to Apache Spark** 
 - Why:Hadoop MapReduce Shortcommings 
   - Only for map and reduce based computations 
   - Relies on reading data from HDFS 
   - Native supprot for java only
   - No interactive shell support 
   - No support for streaming 
 - Basic of Data Analysis with Spark 
   - Expressive programming model 
   - In-memory processing 
   - support for diverse workload 
   - Interactive shell 
  - The Spark Stack: SparkSQL, SparkStreamming, MLlib, GraphX
- Getting Started with Spark: Architecture and Basic Concept 
  - In memory processing: 
    - Spark: the data stores in memory, Resilient distributed databse 
     - RDD: Distributed across the cluster of machine; divided in partitions, atomic chunks of data; Trach history of each partition, re-run. 
    - Spark Architecture: 
      - Driver Program: Spark Context 
      - Cluster manager 
      - Worker Nodes: Executor JVM 
      
4. **Pratice: Spark**
```
# read from HDFS 
lines = sc.textFile("hdfs:/user/cloudera/words.txt")
lines.count()

# split each line into words 
words = line.flatMap(lambda line: line.split(" ")

# Assign inital count value to each word 
tuples = words.map(lambda word: (word,1))

# sum all word count value 
counts = tuples.reduceByKey(lamdba a, b:(a+b))

# write word counts to text file in HDFS 
counts.coalesce(1).saveAsTextFile('hdfs:/user/cloudera/wordcount/outputDir')
# coalesce: combine all RDD partition into a single partition

# view result
hadoop fs - copyToLocal wordcount/outputDir/part-0000 count.txt
more count.txt
```
## Programming in Spark 
1. **Spark Core: Programming in Spark**
   - creating RDD: `lines = sc.textFile("hdfs:/user/cloudera/words.txt")'
   - Apply transformation 
   - perform actions 
2. **Spark Core: Transformations**
   - map: appy function to each element of RDD
  ```
  def lower(line):
      return line.lower()
  lower_text_RDD = text_RDD.map(lower)
  ```
  - faltmap:map then flatten output 
  ```
  def split_words(line):
      return line.split()
  words_RDD = text_RDD.flatMap(split_words)
  words_RDD.collect()
  ```
  - filter: keep only elements where function is true
  ```
  def starts_with_a(word):
      return word.lower().startswith("a")
  words_RDD.filter(starts_with_a).collect()
  ```
  - Coalesce: reduce the number of partitions 
  - Wide Transformations [More Syntax Transformation in Spark](https://spark.apache.org/docs/1.2.0/programming-guide.html#transformations)
    - word count: 
      - key: word, value: frequence 
      - groupByKey 
      - Reduce 
 3. **Spark Core: Actions**
    - Driver program -> RDD-> flatmap -> map -> groupbyKey -> collect by Driver Program 
    - common actions: 
      - take(n): copy first n elements 
      - collect(): copy all elements to the driver 
      - reduce(function): aggregate elements with function 
 4. **Spark SQL** 
   - Why:
     - Enable querying structured and unstructured aata 
     - provide common query language
     - Has APIs for scala, java, python and convert the result to RDD
   - Rational Operations 
   - Connect to variety of database: connects to all BI tools that supprot JDBC, ODBC 
   - Deploy business integllignece tools 
   - How to go relational in spark?
     - step 1: sqlcontext: create dataframe from RDD, HIVE, data source  
     ``` 
     from pyspark.sql import SQLContext
     sqlContext = SQLContext(sc)
     # Jason -> DataFrame 
     df = sqlContext.read.json("/filename.json")
     df.show()
     # register the dataframe as a table 
     df.registerTempTable("Table")
     # run sql 
     Output = sqlContext.sql("select * from Table where...)
      ```
      - dataframe basic 
      ```
      # show table 
      df.show()
      
      # print the schema 
      df.printSchema()
      
      # select only the "X" column 
      df.select("X").show()
      
      # select everybody, but increment the discount by 5% 
      df.select(df['name'],df['discount']+5).show()
      
      # select people height greater than 4.0 ft
      df.filter(df['height'] > 4.0).show()
      
      # count people by zip 
      df.groupBy(zip).count().show()
      ```
5. **Spark MLlib**
   - machine learning library in spark: Distributed implementations  
   - main categories of algo: 
     - machine learning
       - classification, regression, clustering 
       - evaluation metrics 
     ```
     ## Example 1: classification 
     # read and parse data 
     data = sc.textFile("data.txt")
     # decision tree for classification 
     model = DecisionTree.trainClassifier(parsedData, numClasses = 2)
     print(model.toDebugString())
     model.save(sc,"decisionTreeModel")
     
     ## Example 2:clustering 
     data = sc.textFile("data.txt")
     parsedData = data.map(lambda line: array([float(x) for x in line.split(" ")]))
     # k-means model for clustering 
     clusters = Kmeans.train(parsedData, k = 3)
     print(clusters.centers)
     ```
     - stat
       - summary stats, sampling 
      ```
      from pyspark.mllib.stat import Statistics 
      # data as RDD of vector
      dataMatrix = sc.parallelize([[1,2,3,],[4,5,6]])
      # compute column summary stat 
      summary = Statistics.colStats(dataMatrix)
      print(summary.mean(), summary.variance, summary.numNonzeros)
      ```
     - utility for ml pipeline 
       - dimensionality reduction, transformation 
6. **Spark Streamming**  
   - scalable processing for real time analysis, data streams converted to discrete RDDs, 
   - Souce: kafka, flume, HDFS, S3, twitter 
   - create and processing DStreams 
     - Streaming Source: [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
     - Discretize (batch length 2) : [b1,b2,b3,b4,b5] 
     - Transformation(window size: 4, sliding interval:2) [b1,b2],[b2,b3],[b3,b4],[b4,b5](How many entries in 1 unit; how many entris needs to move to next)
7. **Spark GraphX**
   - GraphX is api for graphs and graph-parallel computation 
8. **Spark Practice** 
   ```
   # connect to postgres table 
   
   from pyspark.sql import SQLContext 
   sqlcs = SQLContext(sc)
   df = sqlcs.read.format("jdbc")\
        .option("url","jdbc:postgresql://..)\
        .option("dbtable", "gameclicks")\
        .load()
      
   """
   The format("jdbc") says that the source of the DataFrame will be using a Java database connection, 
   the url option is the URL connection string to access the Postgres database, 
   and the dbtable option specifies the   gameclicks table.
   """
   
   # View Spark DataFrame schema and count rows
   df.printSchema()
   df.count()
   
   #View contents of DataFrame
   df.show(5)
   
   # filter columns in dataframe 
   df.select("userid","teamlevel").show(5)
   
   # filter rows based on criteria 
   df.filter(df['teamlevel']>1).select("userid","teamlevel").show(5)
   
   # group by column and count 
   df.groupBy("ishit").count().show()
   
   # calculate average and sum 
   from pyspark.sql.functions import * 
   df.select(mean('ishit'),sum('ishit')).show()
   
   # join two dataframe 
   df2 = sqlsc.read.format("jdbc")\
        .option("url",..)
        .option("dbtable","adclicks")
        .load()
        
   merge = df.join(df2, 'userid')
   
   ```
   
  

   
 

 


