export const buildMessage = (userInput, userInfo) => {
  const filter = userInfo.filter
  let contextParts = []

  // collect all active filters
  if (filter.date.start && filter.date.end) {
    const startDate = new Date(filter.date.start).toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit'
    })
    const endDate = new Date(filter.date.end).toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit'
    })
    contextParts.push(`I want to travel from ${startDate} to ${endDate}`)
  }

  if (filter.maxPrice) {
    contextParts.push(`My maximum budget is ${filter.maxPrice}€ per person`)
  }

  if (filter.vibe && filter.vibe.length > 0) {
    contextParts.push(`I'm looking for a ${filter.vibe.join(' and ')} experience`)
  }

  if (filter.travelMedium) {
    contextParts.push(`I prefer to travel by ${filter.travelMedium}`)
  }

  if (filter.maxTravelTime) {
    contextParts.push(`The maximum travel time should be ${filter.maxTravelTime} hours`)
  }

  if (filter.personAmount) {
    contextParts.push(`I'm traveling with ${filter.personAmount} ${filter.personAmount === 1 ? 'person' : 'people'}`)
  }

  // build the final message
  let finalMessage = ''

  // add context if available
  if (contextParts.length > 0) {
    finalMessage = `These are the conditions that the trip should meet: ${contextParts.join('. ')}.\n\n`
  }

  // add user input
  finalMessage += `This is my request: ${userInput}. Please answer my request while considering the conditions.`

  return finalMessage
}
