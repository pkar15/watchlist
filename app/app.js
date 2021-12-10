const addMovieModal = document.getElementById('add-modal');
const startAddMovieBtn = document.querySelector('header button');
const backDrop = document.getElementById('backdrop');
const cancelMovieBtn = addMovieModal.querySelector('.btn--passive');
const addMovieBtn = cancelMovieBtn.nextElementSibling;
const userInputs = document.querySelectorAll('input');
const movies = [];
const rootList = document.getElementById('movie-list');
const entryTextSection = document.getElementById('entry-text');
function updateUI () {
    if(movies.length === 0)
    {
        entryTextSection.style.display = 'block';
    }
    else{
        entryTextSection.style.display = 'none';
    }
};
const addMovieBtnHandler = () =>{
    const title = userInputs[0].value;
    const imgUrl = userInputs[1].value;
    const rating = userInputs[2].value;
    if (title.trim() === '' || imgUrl.trim() === '' || rating.trim() === '' ||
    +rating< 1 ||
    +rating >5 )
    {
        alert("Please enter valid user data !!");
    }
    const newMovie = {
        id: Math.random().toString(),
        title: title,
        url: imgUrl,
        rate: rating
    };
    movies.push(newMovie);
    console.log(movies);
    addMovieHandler();
    clearUserInput();
    renderMovieElement(newMovie.id,newMovie.title,newMovie.url,newMovie.rate);
    updateUI();
}
function renderMovieElement (id,title,imgUrl,rating){
    const newList = document.createElement('li');
    newList.className= 'movie-element';
    newList.innerHTML= `
    <div class= 'movie-element__image'>
    <img src='${imgUrl}' alt = '${title}'>;
    </div>
    <div class= 'movie-element__info'>
    <h2>${title}</h2>
    <p> ${rating} / 5 stars</p>
    </div>`;
    rootList.append(newList);
    newList.addEventListener('click',deleteMovieHandler.bind('null',id));
}
function deleteMovieHandler (movieId) {
    let movieIndex=0;
    for(const movie of movies){
        if(movie.id === movieId)
        {break;}
        movieIndex++;
    }
    movies.splice(movieIndex,1);
    rootList.children[movieIndex].remove();
}

const clearUserInput = () => {
    for (const userIP of userInputs)
    {
        userIP.value='';
    }}
const toggleBackDrop = () => {
    backDrop.classList.toggle('visible');
}
const cancelMovieHandler = () => {
     addMovieModal.classList.toggle('visible');
    toggleBackDrop();
}
const addMovieHandler = () =>
{
    addMovieModal.classList.toggle('visible');
    //console.log(addMovieModal);
    toggleBackDrop();
};
startAddMovieBtn.addEventListener('click',addMovieHandler);
backDrop.addEventListener('click',addMovieHandler);
cancelMovieBtn.addEventListener('click',cancelMovieHandler);
addMovieBtn.addEventListener('click',addMovieBtnHandler);
