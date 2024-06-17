
// tmi emulates the color picker behavior in Nuke
// make sure input is linear!

uniform float uT;
uniform float uM;
uniform float uI;

out vec4 fragColor;
void main()
{
	//create vec for input texture
	vec4 color = texture(sTD2DInputs[0], vUV.st);
	
	//apply color temperature adjustment
	color.r *= 1 - (uT / 2);
	color.b *= 1 + (uT / 2);
	
	//apply magenta adjustment
	color.r *= 1 + (uM / 3);
	color.g *= 1 - ((uM * 2) / 3);
	color.b *= 1 + (uM / 3);
	
	//apply intensity adjustment
	color.rgb *= 1 + uI;
	
	//output swizzle
	fragColor = TDOutputSwizzle(color);
}
