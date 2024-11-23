import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserInfoStore = defineStore('userInfo', () => {
  // State
  const filter = ref({
    date: {
      start: null,
      end: null
    },
    maxPrice: 400,
    vibe: [],
    travelMedium: null,
    maxTravelTime: null
  })
  const userInput = ref([])

  // Actions
  const setDate = (newDate) => {
    filter.value.date = newDate
  }

  const setMaxPrice = (price) => {
    filter.value.maxPrice = price
  }

  const setVibe = (newVibe) => {
    filter.value.vibe = newVibe
  }

  const setTravelMedium = (medium) => {
    filter.value.travelMedium = medium
  }

  const setMaxTravelTime = (time) => {
    filter.value.maxTravelTime = time
  }

  const addUserInput = (input) => {
    userInput.value.push(input)
  }

  const removeUserInput = (index) => {
    userInput.value.splice(index, 1)
  }

  return {
    // State
    filter,
    userInput,
    // Actions
    setDate,
    setMaxPrice,
    setVibe,
    setTravelMedium,
    setMaxTravelTime,
    addUserInput,
    removeUserInput
  }
})