<script lang="ts">
    import {Texture} from "pixi.js"
    import {Sprite} from "svelte-pixi"

    import {processedImageAlphaStore, processedImageStore} from "./stores"

    let processedImage: string | null = null

    processedImageStore.subscribe(value => processedImage = value)
</script>

{#if processedImage}
    <Sprite texture={Texture.from(processedImage)} x={0} y={0} width={768} height={768}
            cacheAsBitmap={false}
            alpha={$processedImageAlphaStore}/>
{/if}

<style>
</style>
