<script setup>
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { useChatLogStore } from '@/pinia/chatLog'
import { useUserInfoStore } from '@/pinia/userInfo'
import { useCurrentRecommendationStore } from '@/pinia/currentRecommendation'
import { ref, computed } from 'vue'
import { LoaderCircle, CornerDownRight, Mic } from 'lucide-vue-next'
import axios from 'axios'
import { buildMessage } from '@/interaction/messageBuilder'

const chatLogStore = useChatLogStore()
const userInfoStore = useUserInfoStore()
const recommendationStore = useCurrentRecommendationStore()
const inputValue = ref('')
const isListening = ref(false)

let recognition = null
try {
  // check browser compatibility
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
  recognition = new SpeechRecognition()
  recognition.lang = 'en-US'
  recognition.continuous = false
  recognition.interimResults = false
} catch (e) {
  console.error('Speech Recognition not supported:', e)
}

const startListening = () => {
  if (!recognition) {
    console.error('Speech Recognition not available')
    return
  }

  isListening.value = true
  recognition.start()
}

const stopListening = () => {
  if (recognition) {
    recognition.stop()
    isListening.value = false
  }
}

if (recognition) {
  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript
    inputValue.value = transcript
    stopListening()
    handleSubmit()
  }

  recognition.onerror = (event) => {
    console.error('Speech Recognition Error:', event.error)
    stopListening()
  }

  recognition.onend = () => {
    stopListening()
  }
}

const isWaitingForResponse = computed(() => {
    const messages = chatLogStore.chatLog
    if (messages.length === 0) return false
    const lastMessage = messages[messages.length - 1]
    return lastMessage.user
})

// THIS IS THE FUNCTION FOR THE HTTP REQUEST TO THE BACKEND 
// HANDLING THE INPUT FROM THE USER AND THE RESPONSE FROM THE BACKEND
const handleSubmit = async () => {
    if (inputValue.value.trim() && !isWaitingForResponse.value) {
        try {
            const userMessage = inputValue.value
            chatLogStore.addMessage(userMessage, true)

            const fullMessage = buildMessage(userMessage, userInfoStore)

            const response = await axios.post('http://localhost:8000/chat', {
                input: fullMessage
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })

            if (response.data && response.data.response) {
                chatLogStore.addMessage(response.data.response.answer, false)
                
                recommendationStore.setRecommendation({
                    city: response.data.response.city,
                    country: response.data.response.country,
                    title: response.data.response.title,
                    travelMedium: response.data.response.travelMedium,
                    travelTime: parseFloat(response.data.response.travelTime),
                    price: parseFloat(response.data.response.price),
                    amountPeople: parseInt(response.data.response.amountPeople),
                    amountNights: parseInt(response.data.response.amountNights),
                    imgAddress: response.data.response.imgAddress,
                    description: response.data.response.description
                })

                if (response.data.response.city && 
                    response.data.response.country && 
                    response.data.response.description) {
                    chatLogStore.setHasRecommendation(true)
                }
            }

            inputValue.value = ''
        } catch (error) {
            console.error('Error sending message:', error)
            chatLogStore.addMessage('Sorry, there was an error processing your request.', false)
            inputValue.value = ''
        }
    }
}

const handleKeydown = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault()
        handleSubmit()
    }
}
</script>

<template>
    <Textarea 
        v-model="inputValue" 
        :placeholder="chatLogStore.chatStarted 
            ? 'What else should I consider?' 
            : 'Let me help you plan your trip! What do you want to do?'"
        class="min-h-16" 
        @keydown="handleKeydown" 
        :disabled="isWaitingForResponse" 
    />
    <div class="w-full flex justify-end space-x-2">
        <Button variant="ghost" class="rounded-full" @click="startListening" :disabled="isWaitingForResponse || isListening">
            <LoaderCircle v-if="isListening" class="animate-spin h-4 w-4" />
            <Mic v-else class="h-4 w-4" />
        </Button>
        <Button variant="default" @click="handleSubmit" :disabled="isWaitingForResponse"
            class="bg-[#3C82F6] hover:bg-[#2864c3]">
            <LoaderCircle v-if="isWaitingForResponse" class="animate-spin h-4 w-4" />
            <span v-else class="px-2">
                <CornerDownRight class="h-4 w-4" />
            </span>
        </Button>
    </div>
</template>
