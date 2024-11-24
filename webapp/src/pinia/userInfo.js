import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserInfoStore = defineStore('userInfo', () => {
  // State
  const filter = ref({
    date: {
      start: null,
      end: null
    },
    maxPrice: null,
    vibe: [],
    travelMedium: null,
    maxTravelTime: null,
    personAmount: null
  })
  const userInput = ref([])

  // Actions
  const setDate = (newDate) => {
    filter.value.date.start = newDate.start
    filter.value.date.end = newDate.end
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

  const setPersonAmount = (amount) => {
    filter.value.personAmount = amount
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
    setPersonAmount,
    addUserInput,
    removeUserInput
  }
})