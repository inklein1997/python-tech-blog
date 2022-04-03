const deletePost = async (e) => {
    e.preventDefault();
    const postID = window.location.pathname.split('/').pop();
    const response = await fetch(`/api/posts/${postID}`, {
        method:'DELETE',
        headers: { 'Content-type': 'application/json' }
    })
    if (response.ok) {
        window.location.assign('/dashboard');
    } else {
        alert('Unable to delete post');
    }
}

document.querySelector('#deletePostButton').addEventListener('click', deletePost);