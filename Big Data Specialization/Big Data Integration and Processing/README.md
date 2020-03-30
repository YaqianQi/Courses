# Big Data Integration and Processing
## Data Retrieval
**Data Retrieval** 
**Qeury Language**
**Database Programming Language**
 - Structure Database: 
   -SQL Overview and Syntax  
   - Practice: Querying Relational Data with Postgres
 - Semistructured Database: MongoDB 
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
   - Practice Query Documents in MongoDB 
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
 

 


