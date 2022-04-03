const postSelection = document.querySelectorAll('.post_title');

postSelection.forEach(post => post.addEventListener('click', (e) => {
    window.location.assign(`/thread/${e.target.getAttribute('data-post-id')}`);
}));