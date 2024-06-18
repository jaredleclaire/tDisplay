//a fragment shader for basic grading controls 

uniform float uTemperature;
uniform float uMagenta;
uniform float uIntensity;
uniform vec4 uLift;
uniform vec4 uGamma;
uniform vec4 uGain;
uniform vec4 uOffset;
uniform float uSaturation;

out vec4 fragColor;

float LinearToACEScc(float lin) 
{    
    if (lin <= 0.0) 
        return -0.3584474886;
    
    if (lin < exp2(-15.0))
    	return log2(exp2(-16.0) + lin * 0.5) / 17.52 + (9.72/17.52);
    
    return log2(lin) / 17.52 + (9.72/17.52);
}

float ACESccToLinear(float cc) 
{
    if (cc < -0.3013698630)
    	return exp2(cc * 17.52 - 9.72)*2.0 - exp2(-16.0)*2.0;
    
    return exp2(cc * 17.52 - 9.72);
}

void main()
{
	//input texture
	vec4 color = texture(sTD2DInputs[0], vUV.st);
	
	//temperature
	color.r *= 1 - (uTemperature / 2);
	color.b *= 1 + (uTemperature / 2);
	
	//magneta
	color.r *= 1 + (uMagenta / 3);
	color.g *= 1 - ((uMagenta * 2) / 3);
	color.b *= 1 + (uMagenta / 3);
	
	//intensity
	color.rgb *= 1 + uIntensity;
	
	//lin2log
	vec3 ACESccColor = vec3(LinearToACEScc(color.r),LinearToACEScc(color.g),LinearToACEScc(color.b));
	
	color.rgb = ACESccColor.rgb;
	
	//LGG
	vec3 lift = uLift.rgb;
	float liftLevel = uLift.a;
	lift += liftLevel;
	
	vec3 gamma = uGamma.rgb;
	float gammaLevel = uGamma.a;
	gamma += gammaLevel;
	
	vec3 gain = uGain.rgb;
	float gainLevel = uGain.a;
	gain += gainLevel;
	
	vec3 offset = uOffset.rgb;
	float offsetLevel = uOffset.a;
	offset += offsetLevel;
	
	color.rgb = pow(max(vec3(0.0), color.rgb * (1.0 + gain - lift) + lift + offset), max(vec3(0.0), 1.0 - gamma));
	
	//saturation
	vec3 hsv;
	hsv.xyz = TDRGBToHSV(color.rgb);
	hsv.y *= uSaturation;
	color.rgb = TDHSVToRGB(hsv.xyz);
	
	//log2lin
	vec3 linearColor = vec3(ACESccToLinear(color.r),ACESccToLinear(color.g),ACESccToLinear(color.b));
	
	//handoff
	color.rgb = linearColor.rgb;
	
	//output swizzle
	fragColor = TDOutputSwizzle(color);
}
