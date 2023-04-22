<script lang="ts">
    import {imageStore} from "./stores"

    let image: string | null = null

    imageStore.subscribe(value => image = value)
</script>

<section class="image-container">
    <img src="{image}" class:empty={!image} />
</section>

<style>
    .image-container {
        @apply flex flex-row items-center justify-center;
    }

    img.empty {
        @apply min-w-[90vw] min-h-[90vh] max-w-[90vw] max-h-[90vw];
    }

    img:not(.empty) {
        --size-w: min(1024px, 90vw);
        --size-h: min(1024px, 90vh);

        @apply max-w-[--size-w] max-h-[--size-h] aspect-auto select-none rounded-md;
    }
</style>
