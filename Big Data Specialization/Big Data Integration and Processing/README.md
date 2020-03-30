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
      - Operation: 
      `$eq, $gt, $gte, $lt, $lte, $ne, $in, $nin, $or, $and, $not, $nor`
      - Array Operation: 
        - find itens which are tagged `db.inventory.find({tags:{$in:["popular", "organic"]}})`
        - find 2nd and 3rf element of tags `db.inventory.find({},{tags:{$slice:[1,2]}) -- skip 1, and return 2 rows`
        - find document whose 2nd element in tag is "summer`db.inventory.find(tags.1:"summer")`
      - Example: 
     `select distinct beer, price from sells where price > 15`
     `db.sells.distinct({price:{$gt:15}, {beer:1, price:1,_id:0}})`
   
 
 
 
