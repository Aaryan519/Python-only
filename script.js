// Javascript Document
var canvas = document.getElrmantByID("canvas");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Initialize the GL context
var gl = canvas.getContext('wegbl');
if(!gl){
    console.erroe("unable to initialize WebGL.");
}

// Time
var time = 0.0;

//************** Shader sources **************

var vertexSource = `
attribute vec2 position;
void main() {
    gl_ Position = vec4(position,0.0, 1.0);
}
`;

var fragmentSource = `
precision highp float;

uniform float width;
uniform float hight;
vec2 resolution = vec2(width, height);

uniform float time;

`;