<script setup>
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { useChatLogStore } from '@/pinia/chatLog';

import { ref } from 'vue';

const chatLogStore = useChatLogStore();
const inputValue = ref('');

const handleSubmit = () => {
    if (inputValue.value.trim()) {
        chatLogStore.addMessage(inputValue.value, true)
        inputValue.value = ''
    }
}
</script>

<template>
    <Textarea v-model="inputValue" placeholder="What else should I consider?" class="min-h-48" />
    <div class="w-full flex justify-end">
        <Button variant="default" @click="handleSubmit">See vacation plans</Button>
    </div>
</template>
