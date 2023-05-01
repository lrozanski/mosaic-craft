<script lang="ts">
    import {processedImageAlphaStore} from "./stores"
</script>

<div class="image-toolbar">
    <div class="flex flex-row items-center justify-evenly space-x-2">
        <label for="alpha">Overlay Alpha</label>
        <input id="alpha" type="range" min="0.0" max="1.0" step="0.01" bind:value={$processedImageAlphaStore}>
        <span class="w-10 text-center">{$processedImageAlphaStore}</span>
    </div>
</div>

<style>
    .image-toolbar {
        @apply flex flex-row items-center justify-evenly min-w-[18rem] h-12 bg-slate-600 rounded mt-3 px-3 space-x-2;
    }
</style>
