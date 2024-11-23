<script setup>
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
</script>

<template>
    <Textarea placeholder="What else should I consider?" class="min-h-48" />
    <div class="w-full flex justify-end">
        <Button variant="default">See vacation plans</Button>
    </div>
</template>
