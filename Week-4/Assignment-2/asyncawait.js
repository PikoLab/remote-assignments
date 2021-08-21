function getPost(posts){
    const html= posts.map((post)=>{
        return `
        <div class="post">
            <p>Name: <strong> ${post.name}</strong></p>
            <p>Price: ${post.price}</p>
            <p>Description: ${post.description}</p>
        </div>
        `
    }).join("")
    document.querySelector("#result").insertAdjacentHTML("afterbegin",html);
}

async function createPost(url, callback){
    const res = await fetch(url,{
        method:"GET",
        headers:{
            'content-type': 'application/json'
        },
    });

    const data = await res.json();
    callback(data)
}


createPost('http://13.230.176.178:4000/api/1.0/remote-w4-data', getPost)