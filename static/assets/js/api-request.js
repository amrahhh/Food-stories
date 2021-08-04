const subscribeForm = document.getElementById('subscribe-section');
const domain = 'http://localhost:8000'
// const formErrorField = subscribeForm.querySelector('#form-error');


//  ----------------  SUBSCRIBE FORM ----------------------


subscribeForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    let formData = {
        email: subscribeForm.email.value, 
    }
    let response = await fetch(domain + window.URLS['subscribeUrl'], {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });

    let responseData = await response.json()
    if (response.ok) {
        subscribeForm.email.value = '';
        // formErrorField.classList.remove('text-danger');
        // formErrorField.classList.add('text-success');
        myFunction('Siz abune oldunuz')
    }
    else {
        // formErrorField.classList.remove('text-success');
        // formErrorField.classList.add('text-danger');
        myFunction(responseData.email)
    }

});


// window.addEventListener("load", async function () {

//     let response = await fetch(domain + window.URLS['recipeDetail'], {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//         },

//     });
//     let responseData = await response.json()
//     if (response.ok) {
//         let commenCountElement = document.getElementById('comment-count')
//         commenCountElement.innerText = responseData['comment_count'];
//     }
//     else {
//         myFunction('Something went wrong!')
//     }

// });