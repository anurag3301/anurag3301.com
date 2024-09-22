+++
insert_anchor_links = "right"
title = ""
+++

{% crt() %}
```
                                            __________ ____ ___
         ____ _____  __  ___________ _____ |__  /__  // __ <  /
        / __ `/ __ \/ / / / ___/ __ `/ __ `//_ < /_ </ / / / / 
       / /_/ / / / / /_/ / /  / /_/ / /_/ /__/ /__/ / /_/ / /  
       \__,_/_/ /_/\__,_/_/   \__,_/\__, /____/____/\____/_/   
                                   /____/                      
```
{% end %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<table>
    <tr>
        <th><a target=_blank href="https://github.com/anurag3301">
            {{bsicon(color="white", class="bi bi-github")}} Github</a>
        </th>
        <th><a target=_blank href="https://www.linkedin.com/in/anurag3301/">
            {{bsicon(color="#0a66c2", class="bi bi-linkedin")}} LinkedIn</a>
        </th>
        <th><a target=_blank href="https://www.youtube.com/@anurag3301YT">
            {{bsicon(color="#ff4545", class="bi bi-youtube")}} Youtube</a>
        </th>
        <th><a target=_blank href="/resume">
            {{bsicon(color="white", class="bi bi-file-earmark-person-fill")}} Resume</a>
        </th>
        <th><a target=_blank href="/blog">
            {{bsicon(color="white", class="bi bi-newspaper")}} Blog</a>
        </th>
    </tr>
</table>

<br>

I’m an embedded systems engineer with two years of experience in programming and electronics. Proficient in Python, C++, Bash, and Lua, I’ve worked with AVR microcontrollers and am currently exploring ARM Cortex-M with STM32 and FreeRTOS using ESP-IDF. A Linux enthusiast, I configure and use Arch Linux for my projects. I also write blog, make sure to check them out {{anchor(url="/blog", title="here")}}.

# Projects

## STM32 pio libs
> Check the project {{anchor(url="https://github.com/STM32-pio-libs", title="Link")}}

I’ve launched a GitHub organization focused on developing and publishing drivers for sensors and modules with STM32Cube HAL. This effort bridges the gap for components with Arduino libraries but lacking STM32 HAL support. These libraries are easily installable through {{anchor(url="https://registry.platformio.org/search?q=owner%3Aanurag3301", title="PlatformIO registery", code=true)}}.

#### Drivers Written So Far

1. Real Time clock: {{anchor(url="https://github.com/STM32-pio-libs/DS1302-RTC", title="DS1302 RTC")}}
2. I2C for 1602 LCD: {{anchor(url="https://github.com/STM32-pio-libs/I2C-LCD", title="PCF8574")}}
3. GPS: {{anchor(url="https://github.com/STM32-pio-libs/NEO-6M", title="NEO-6M")}}
4. Ultrasonic distance: {{anchor(url="https://github.com/STM32-pio-libs/HC-SR04", title="HC-SR04")}}

<br>

## nvim-platformio.lua

> Check the project {{anchor(url="https://github.com/anurag3301/nvim-platformio.lua", title="Link")}}

A Neovim extension for PlatformIO that provides a streamlined project management experience, akin to the official VSCode extension. This plugin integrates with Telescope to make searching for libraries and development board MCUs straightforward, enhancing Neovim’s capabilities for embedded system development. With over 60 stars on GitHub and contributions from three collaborators, it’s gained notable traction.

#### Project Explaination
{{youtube(id="Jcqat7NhXrc")}}
