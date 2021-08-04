const recipeEditForm = document.getElementById('recipe-edit-section');


function myFunction(e) {
    var x = document.getElementById("snackbar");
    x.innerText = e

    x.className = "show";

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

// ----------------- GET RECIPE DATA --------------------

window.addEventListener('load', async function () {

    let response = await fetch(domain + window.URLS['updateRecipe']);
    if (response.ok) {
        data = await response.json();
        recipeEditForm.title.value = data.title;
        recipeEditForm.short_description.value = data.short_description;
        recipeEditForm.description.value = data.description;
        recipeEditForm.image.files[0] = data.image;
        recipeEditForm.category.value = data.category;
        recipeEditForm.tags.value = data.tags;
    }
});

//  ------------------ EDIT RECIPE ------------------------

document.querySelector('#recipe-edit-section').addEventListener('submit', async (e) => {
    e.preventDefault();
    let form = e.target;
    let postData = new FormData(form);
    postData.append('title', form.title.value);
    postData.append('short_description', form.short_description.value);
    postData.append('description', form.description.value);
    postData.append('image', form.image.files[0]);
    postData.append('category', form.category.value);
    postData.append('tags', form.tags.value);

    let response = await fetch(domain + window.URLS['updateRecipe'], {
        headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
        },
        method: "PUT",
        body: new FormData(form)
    });

    data = await response.json();

    if (response.ok) {
        myFunction('Recipe editted...')

    }
    else {
        myFunction('Something went wrong')
    }
})

