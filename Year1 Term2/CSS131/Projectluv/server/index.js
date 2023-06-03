const express = require('express')
const cors = require('cors')
const app = express()
const port = 3000
const { MongoClient } = require("mongodb");
const uri = "mongodb+srv://admin123:1234@al.bypkkj6.mongodb.net/";

app.use(cors())
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})

console.log('Hello World');

app.post('/classschedule/create', async (req, res) => {
    const classsub = req.body;
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Class').insertOne({
        id: parseInt(classsub.id),
        namesubject: classsub.namesubject,
        classsite: classsub.classsite,
        day: classsub.day,
        time: parseInt(classsub.time),
        mintime: parseInt(classsub.mintime),


    });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + classsub.id + " is created",
        "classsub": classsub
    });
})

app.get('/classschedule', async (req, res) => {
    const id = parseInt(req.params.id);
    const client = new MongoClient(uri);
    await client.connect();
    const classsub = await client.db('mydb').collection('Class').find({}).toArray();
    await client.close();
    res.status(200).send(classsub);
})

app.get('/classschedule/:id', async (req, res) => {
    const id = parseInt(req.params.id);
    const client = new MongoClient(uri);
    await client.connect();
    const classsub = await client.db('mydb').collection('Class').findOne({ "id": id });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "classub": classsub
    });
})

app.put('/classschedule/update', async (req, res) => {
    const classsub = req.body;
    const id = parseInt(classsub.id);
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Class').updateOne({ 'id': id }, {
        "$set": {
            id: parseInt(classsub.id),
            namesubject: classsub.namesubject,
            classsite: classsub.classsite,
            day: classsub.day,
            time: parseInt(classsub.time),
            mintime: parseInt(classsub.mintime),
        }
    });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + id + " is updated",
        "classsub": classsub
    });
})

app.delete('/classschedule/delete', async (req, res) => {
    const id = parseInt(req.body.id);
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Class').deleteOne({ 'id': id });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + id + " is deleted"
    });
})

// Homework
app.post('/homewrk/create', async (req, res) => {
    const homewrk = req.body;
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Homework').insertOne({
        id: parseInt(homewrk.id),
        namework: homewrk.namework,
        day: parseInt(homewrk.day),
        month: parseInt(homewrk.month),
        hour: parseInt(homewrk.hour),
        minute: parseInt(homewrk.minute),



    });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + homewrk.id + " is created",
        "homewrk": homewrk
    });
})


app.get('/homewrk', async (req, res) => {
    const id = parseInt(req.params.id);
    const client = new MongoClient(uri);
    await client.connect();
    const homewrk = await client.db('mydb').collection('Homework').find({}).toArray();
    await client.close();
    res.status(200).send(homewrk);
})

app.get('/homewrk/:id', async (req, res) => {
    const id = parseInt(req.params.id);
    const client = new MongoClient(uri);
    await client.connect();
    const homewrk = await client.db('mydb').collection('Homework').findOne({ "id": id });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "homewrk": homewrk
    });
})

app.put('/homewrk/update', async (req, res) => {
    const homewrk = req.body;
    const id = parseInt(homewrk.id);
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Homewrk').updateOne({ 'id': id }, {
        "$set": {
            id: parseInt(homewrk.id),
            namework: homewrk.namework,
            day: parseInt(homewrk.day),
            month: parseInt(homewrk.month),
            hour: parseInt(homewrk.hour),
            minute: parseInt(homewrk.minute),
        }
    });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + id + " is updated",
        "homewrk": homewrk
    });
})

app.delete('/homewrk/delete', async (req, res) => {
    const id = parseInt(req.body.id);
    const client = new MongoClient(uri);
    await client.connect();
    await client.db('mydb').collection('Homework').deleteOne({ 'id': id });
    await client.close();
    res.status(200).send({
        "status": "ok",
        "message": "User with ID = " + id + " is deleted"
    });
})