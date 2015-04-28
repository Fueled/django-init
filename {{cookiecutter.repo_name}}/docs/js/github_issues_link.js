// Requires: https://padolsey.github.io/findAndReplaceDOMText/src/findAndReplaceDOMText.js

var github_repo = '{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}';
findAndReplaceDOMText(document.querySelector('[role="main"]'), {
  find: /#(\d+)/g,
  replace: function(portion, match){
    var el = document.createElement("a");
    el.setAttribute('href', 'http://github.com/'+ github_repo +'/issues/'+ match[1]);
    el.setAttribute('target', '_blank');
    el.innerHTML = portion.text;
    return el;
    }
});
