const express=require('express');
const fs=require('fs');
const bodyParser=require('body-parser');
var spawn=require('child_process').spawn;

let app= express();
app.use(express.static(__dirname));

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());

app.get('/',function(req,res){
    res.render(index.html);
});
app.post('/image',function(req,res){
    let img=req.body.url;
    let data = img.replace(/^data:image\/\w+;base64,/, "");
    let buf = new Buffer(data, 'base64');
    fs.writeFile('image.png', buf);
    let buf1;
    var test=spawn('python',['run.py','image.png']);
    test.stdout.on('data', function(data) {
        buf1=data.toString();
        res.send(buf1);
    } );
    
});


app.listen(3000, () => {
  console.log('Server is up on port 3000');
});




