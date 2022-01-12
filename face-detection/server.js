const express = require('express')
const cors = require('cors')

const app = express()
app.use(cors())

app.get("/prediction", function(request, response) { 
    let artist = request.query.artist
    
    if (artist === 0) {
        // let image = 
    }
    else {
    
    }  
})

const port = 5000;
app.listen(port, () => `Server running on port ${port}`)