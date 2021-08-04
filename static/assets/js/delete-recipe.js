document.querySelector(".delete-event").addEventListener("click", deleteMethod);

function deleteMethod(e) {
    e.preventDefault();
    let recipeId = e.target.dataset.id
    console.log(e.target)
    const deleteMethod = {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
        },
    }
    fetch('http://localhost:8000/az/api/recipes/'+ recipeId, deleteMethod)
        .then(response => response.json())
        
    .then(() => location.reload())
        
}