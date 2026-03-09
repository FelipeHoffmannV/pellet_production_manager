// Rota de login para usuario / operador
document.querySelectorAll('.user-btn').forEach(button => {
    button.addEventListener('click', function(){
        window.location.href = this.dataset.url;
    })
})


// Rota de login para adm
document.querySelectorAll('.admin-btn').forEach(button => {
    button.addEventListener('click', function(){
        window.location.href = this.dataset.url;
    })
})