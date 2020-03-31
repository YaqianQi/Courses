# Big Data Integration and Processing
## Data Retrieval
**Data Retrieval** 
**Qeury Language**
**Database Programming Language**
 1. Structure Database: 
   - SQL Overview and Syntax  
   - Practice: Querying Relational Data with Postgres
 2. Semistructured Database: MongoDB 
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
  3. Practice Query Documents in MongoDB 
     - Exploring pandas dataframe 
 
## Information Integration 
- Data Fusion: Using data from subset of souces find the true value or true value distribution of a data item

## Processing Big Data 
- A Dataflow Approach 
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
   - Fileter: select elements that match a criteria 
 - Aggregations in Big Data Pipeline 
   - What is aggregation: 
     - group by, average, min, max, standard deviation, and, or, 
     - union, intersection, difference, concatenation
 - Analytical Operations: Pattern -> insights -> Decision 
   - Purpose: discover meaningful trends and patterns in data; gain insights into problem; make data-driven decison 
   - Sample Analytical Operation: Classification; Clustering; Path analysis; Connectivity analysis 
- Overview of Big Data Processing Systems
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
  - Introduction to Apache Spark 
    - Why spark:Hadoop MapReduce Shortcommings 
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
         
       
 
   
 

 


