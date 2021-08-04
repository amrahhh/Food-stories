const recipeForm = document.getElementById('recipe-section');
const recipeEditForm = document.getElementById('recipe-edit-section');
// const domain = 'http://localhost:8000'

//  ----------------  SNACKBAR ----------------------

function myFunction(e) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");
    x.innerText = e

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
}


//  ---------------- DATA TAG  ----------------------

window.addEventListener("load", async function () {

    let response = await fetch(domain + '/az/api/tags/');
    if (response.ok) {
        data = await response.json();
        tag_select_id = document.getElementById('tags');
        let options = '';
        data.forEach(element => {
            options += `<option value="${element.id}">${element.title}</option>`
        });
        tag_select_id.innerHTML = options
    }

});

//  ---------------- DATA CATEGORY  ----------------------

window.addEventListener("load", async function () {

    let response = await fetch(domain + '/az/api/category/');
    if (response.ok) {
        data = await response.json();
        category_select_id = document.getElementById('category');
        let options = '';
        data.forEach(element => {
            options += `<option value="${element.id}">${element.title}</option>`
        });
        category_select_id.innerHTML = options
    }

});

//  ---------------- RECIPE FORM --------------------

recipeForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    let formData = new FormData()
    formData.append('title', recipeForm.title.value)
    formData.append('short_description', recipeForm.short_description.value)
    formData.append('description', recipeForm.description.value)
    formData.append('image', recipeForm.image.files[0])
    formData.append('category', recipeForm.category.value)
    formData.append('tags', recipeForm.tags.value)

    let response = await fetch(domain + window.URLS['recipeUrl'], {
        method: 'POST',
        headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
            // 'Content-Type': 'application/json',
        },
        body: formData
    });

    let responseData = await response.json()
    if (response.ok) {
        recipeForm.title.value = '';
        recipeForm.short_description.value = '';
        recipeForm.description.value = '';
        recipeForm.image.value = '';
        myFunction('Recipe added...')
    }
    else {
        myFunction(responseData.title)
    }

});