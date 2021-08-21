function getPost(posts){
    const html= posts.map((post)=>{
        return `
        <div class="post">
            <p>Name: <strong>${post.name}</strong></p>
            <p>Price: ${post.price}</p>
            <p>Description: ${post.description}</p>
        </div>
        `
    }).join("")
    document.querySelector("#result").insertAdjacentHTML("afterbegin",html);
}

function createPost(url){
    return new Promise ((resolve,reject)=>{
        const error = false
        if (!error){
            resolve(
                fetch(url,{
                    method:"GET",
                    headers:{
                        'content-type': 'application/json'
                    },
                })
                .then(res => res.json())
            )
        } else {
            reject('Error: Something went wrong!')
        }
    })
}

createPost('http://13.230.176.178:4000/api/1.0/remote-w4-data')
.then(getPost)
.catch(error => console.log(error))