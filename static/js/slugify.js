// static/js/slugify.js
document.addEventListener('DOMContentLoaded', function() {
    var titleInput = document.getElementById('id_tittle');
    var slugInput = document.getElementById('id_slug');
  
    titleInput.addEventListener("input", function() {
      var slug = titleInput.value
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)/g, '');
  
      slugInput.value = slug;
    });
  });
  