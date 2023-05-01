<script lang="ts">
    import {processedImageAlphaStore} from "./stores"

    let processedImageAlpha: number

    processedImageAlphaStore.subscribe(value => processedImageAlpha = value)

    const updateZoom = (e: Event) => {
        const input = e.currentTarget as HTMLInputElement

        processedImageAlphaStore.set(+input.value)
    }
</script>

<div class="image-toolbar">
    <label for="alpha">Overlay Alpha</label>
    <input id="alpha" type="range" min="0.0" max="1.0" step="0.01" bind:value={$processedImageAlphaStore}>
    <span class="w-10 text-center">{processedImageAlpha}</span>
</div>

<style>
    .image-toolbar {
        @apply flex flex-row items-center justify-evenly min-w-[18rem] h-12 bg-slate-600 rounded mt-3 px-3 space-x-2;
    }
</style>
