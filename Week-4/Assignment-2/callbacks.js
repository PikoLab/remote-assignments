function getPost(posts){
    const html= posts.map((post)=>{
        return `
        <div class="post">
            <p class="name">Name: <strong> ${post.name}</strong></p>
            <p>Price: ${post.price}</p>
            <p>Description: ${post.description}</p>
        </div>
        `
    }).join("")
    document.querySelector("#result").insertAdjacentHTML("afterbegin",html);
}

function createPost(url, callback){
    fetch(url,{
    method:"GET",
    headers:{
        'content-type': 'application/json'
    },
})
    .then(res => res.json())
    .then(data =>{
        callback(data)
    })
    .catch(err => console.log(err))
}

createPost('http://13.230.176.178:4000/api/1.0/remote-w4-data', getPost)