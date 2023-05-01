<script lang="ts">
    import {Texture} from "pixi.js"
    import {Application, Sprite} from "svelte-pixi"
    import Overlay from "./Overlay.svelte"
    import {imageStore} from "./stores"

    let image: string | null = null

    imageStore.subscribe(value => image = value)
</script>

<section class="image-container">
    {#if image}
        <Application width={768} height={768} antialias render="demand" on:postrender={() => console.log('render')}>
            <Sprite texture={Texture.from(image)} x={0} y={0} width={768} height={768} />
            <Overlay />
        </Application>
    {/if}
</section>

<style>
    .image-container {
        @apply flex flex-row items-center justify-center w-[768px] h-[768px] border border-slate-600;
    }
</style>
