let util = {

}
util.title = function(title){
    title = title ? title + '-LightBlog' : 'LightBlog';
    window.document.title = title;
}

export default util;