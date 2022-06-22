export interface PaginationResponse<T> {
    count: number,
	page_size: number,
	next: string | null,
	previous: string | null,
	results: T[]
}
