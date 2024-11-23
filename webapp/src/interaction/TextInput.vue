<script setup>
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { useChatLogStore } from '@/pinia/chatLog'
import { ref, computed } from 'vue'
import { LoaderCircle } from 'lucide-vue-next'
import axios from 'axios'

const chatLogStore = useChatLogStore()
const inputValue = ref('')

const isWaitingForResponse = computed(() => {
  const messages = chatLogStore.chatLog
  if (messages.length === 0) return false
  const lastMessage = messages[messages.length - 1]
  return lastMessage.user
})

const handleSubmit = async () => {
  if (inputValue.value.trim()) {
    try {
      chatLogStore.addMessage(inputValue.value, true)
      
      const response = await axios.post('http://localhost:8000/chat', {
        input: inputValue.value
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      
      if (response.data && response.data.response) {
        chatLogStore.addMessage(response.data.response, false)
      }
      
      inputValue.value = ''
    } catch (error) {
      console.error('Error sending message:', error)
      chatLogStore.addMessage('Sorry, there was an error processing your request.', false)
      inputValue.value = ''
    }
  }
}
</script>

<template>
    <Textarea v-model="inputValue" placeholder="What else should I consider?" class="min-h-48" />
    <div class="w-full flex justify-end">
      <Button variant="default" @click="handleSubmit" :disabled="isWaitingForResponse" class="bg-[#3C82F6] hover:bg-[#2864c3]">
        <LoaderCircle v-if="isWaitingForResponse" class="animate-spin h-4 w-4" />
        <span v-else>See vacation plans</span>
      </Button>
    </div>
</template>
