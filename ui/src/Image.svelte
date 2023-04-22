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

    img {
        @apply aspect-auto select-none rounded-md;
    }

    img.empty {
        @apply min-w-[512px] min-h-[512px] max-w-[90vw] max-h-[90vw];
    }

    img:not(.empty) {
        @apply max-w-[90vw] max-h-[90vh];
    }
</style>
