<script lang="ts">
    import {Texture} from "pixi.js"
    import {Application, Graphics, Sprite} from "svelte-pixi"
    import {imageStore, processedImageStore} from "./stores"

    let image: string | null = null
    let processedImage: string | null = null

    imageStore.subscribe(value => image = value)
    processedImageStore.subscribe(value => processedImage = value)
</script>

<section class="image-container">
    {#if image}
        <Application width={768} height={768} antialias render="demand" on:postrender={() => console.log('render')}>
            <Sprite texture={Texture.from(image)} x={0} y={0} width={768} height={768} />
            {#if processedImage}
                <Sprite texture={Texture.from(processedImage)} x={0} y={0} width={768} height={768} alpha={0.5} />
            {/if}
        </Application>
    {/if}
</section>

<style>
    .image-container {
        @apply flex flex-row items-center justify-center w-[768px] h-[768px] border border-slate-600;
    }
</style>
