uniform float time;
uniform float surface_y;
uniform float wave_height;
uniform float wave_length;
uniform float wave_speed;

void main(void)
{
    float pi = 3.14159265358979323846264;
    vec2 tex_coord = vec2(gl_TexCoord[0]);
    float x = tex_coord.x;
    float y = tex_coord.y;
    if (y < surface_y + 0.5 * wave_height) {
        if (y < surface_y - 0.5 * wave_height) {
            gl_FragColor = gl_Color;
        } else if (y < surface_y + 0.2 * wave_height -
                   0.7 * wave_height * abs(sin(2.0 * pi * -wave_speed * time + 2.0 * pi * x / wave_length)) +
                   0.3 * wave_height * pow(sin(4.0 * pi * -wave_speed * time + pi * x / wave_length), 2.0))
        {
            gl_FragColor = gl_Color;
        }
    }
}
