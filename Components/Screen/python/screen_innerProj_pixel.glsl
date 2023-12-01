uniform float uShadowStrength;
uniform vec3 uShadowColor;
uniform vec4 uDiffuseColor;
uniform vec4 uAmbientColor;
uniform vec3 uSpecularColor;
uniform float uShininess;


in Vertex
{
	vec4 color;
	vec3 worldSpacePos;
	vec3 worldSpaceNorm;
	flat int cameraIndex;
} iVert;

// Output variable for the color
layout(location = 0) out vec4 oFragColor[TD_NUM_COLOR_BUFFERS];
void main()
{
	// This allows things such as order independent transparency
	// and Dual-Paraboloid rendering to work properly
	TDCheckDiscard();

	vec4 outcol = vec4(0.0, 0.0, 0.0, 0.0);
	
	// get projection texture from light 0
	vec4 projColor = TDProjMap(0, iVert.worldSpacePos, vec4(0,0,0,0));

	outcol = projColor;

	// Alpha Calculation
	float alpha = projColor.a * iVert.color.a ;

	// Dithering, does nothing if dithering is disabled
	outcol = TDDither(outcol);

	//alpha premult - BYPASS TO AVOID DARK FRINGING ON COMPOSITES
	//outcol.rgb *= alpha;

	// Modern GL removed the implicit alpha test, so we need to apply
	// it manually here. This function does nothing if alpha test is disabled.
	TDAlphaTest(alpha);

	outcol.a = alpha;
	oFragColor[0] = TDOutputSwizzle(outcol);


	// TD_NUM_COLOR_BUFFERS will be set to the number of color buffers
	// active in the render. By default we want to output zero to every
	// buffer except the first one.
	for (int i = 1; i < TD_NUM_COLOR_BUFFERS; i++)
	{
		oFragColor[i] = vec4(0.0);
	}
}
