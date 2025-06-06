def turing_machine_tape(tape):
    head = 1  # İlk '#'
    state = 'start'
    print("Başlangıç:", ''.join(tape))

    while state != 'accept' and state != 'reject':
        print(f"[{state}] Bant: {''.join(tape)}  (Pozisyon: {head})")

        if state == 'start':
            if tape[head].isdigit():
                state = 'check'
            else:
                state = 'reject'

        elif state == 'check':
            if tape[head] == '#':
                state = 'verify_done'
                head += 1
            elif tape[head].isdigit():
                current_digit = tape[head]
                # Sistem PIN'ine git ve eşleşme kontrol et
                sep_index = tape.index('#', 1)
                match_index = sep_index + 1

                while match_index < len(tape) and tape[match_index] in ['X', 'Y']:
                    match_index += 1

                if tape[match_index] == current_digit:
                    tape[head] = 'X'  # Kullanıcı PIN'inde işaretle
                    tape[match_index] = 'Y'  # Sistem PIN'inde işaretle
                    head += 1
                else:
                    state = 'reject'

        elif state == 'verify_done':
            # Karakter kalmış mı, hepsi işaretli mi kontrol et
            for ch in tape:
                if ch.isdigit():
                    state = 'reject'
                    break
            else:
                state = 'accept'

    print(f"[{state.upper()}] Son Bant: {''.join(tape)}")
    if state == 'accept':
        print("✅ Şifre doğru")
    else:
        print("❌ Şifre hatalı")


def main():
    user_pin = input("4 haneli PIN girin: ")
    system_pin = "1234"

    if len(user_pin) != 4 or not user_pin.isdigit():
        print("Geçersiz PIN formatı.")
        return

    # Bant: #1234#1234#
    tape = list(f"#{user_pin}#{system_pin}#")
    turing_machine_tape(tape)


if __name__ == "__main__":
    main()
