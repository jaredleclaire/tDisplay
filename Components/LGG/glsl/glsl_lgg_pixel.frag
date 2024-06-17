// pixel shader for lift gamma gain color grading

uniform vec3 uLift;
uniform vec3 uGamma;
uniform vec3 uGain;
uniform vec3 uOffset;

out vec4 fragColor;
void main()
{
	vec4 color = texture(sTD2DInputs[0], vUV.st);
	color.rgb = pow(max(vec3(0.0), color.rgb * (1.0 + uGain - uLift) + uLift + uOffset), max(vec3(0.0), 1.0 - uGamma));
	fragColor = TDOutputSwizzle(color);
}
