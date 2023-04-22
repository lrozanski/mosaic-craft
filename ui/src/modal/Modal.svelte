<script lang="ts">
</script>

<div class="modal-container">
    <div role="dialog" class="modal">
        <slot />
    </div>
</div>

<style>
    .modal-container {
        @apply fixed inset-0 bg-black opacity-30;
    }

    .modal {
        @apply m-auto bg-white rounded;
    }
</style>
