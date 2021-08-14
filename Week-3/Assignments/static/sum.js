const n=document.querySelector('#n');
const form=document.querySelector('form');
const result=document.querySelector('#result');


form.addEventListener('submit', (event)=>{
    result.innerHTML = ""
    n_value=n.value

    let request_options={
        method:"GET",
        headers:{
            'content-type': 'application/json'
        },
    }

    fetch(`/data?number=${n_value}`,request_options)
    .then(response=> response.json())
    .then((data)=>{
        console.log(data)
        result.innerHTML += `<p>${data.result}</p>`
        form.reset()
    })
    .catch((err)=>{console.log(err)});

    event.preventDefault();
})